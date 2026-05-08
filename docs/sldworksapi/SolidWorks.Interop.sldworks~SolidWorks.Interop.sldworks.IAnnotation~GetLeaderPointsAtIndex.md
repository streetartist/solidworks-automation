# GetLeaderPointsAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderPointsAtIndex`

Gets coordinate information about a specified leader on this annotation.
Gets coordinate information about a specified leader on this annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLeaderPointsAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As IAnnotation
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetLeaderPointsAtIndex(Index)
```

```

System.object GetLeaderPointsAtIndex( 
   System.int Index
)
```

```

System.Object^ GetLeaderPointsAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of leader within this annotation (see **Remarks**)

#### Return Value

Array of objects (see **Remarks**)

Remarks

The index value is 0-based. Therefore, a valid index value is >= 0 < number of leaders on this annotation.

Use [IAnnotation::GetLeaderCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderCount.md) to find out how many leaders are on this annotation. If the index value is invalid in Visual Basic for Applications (VBA), SOLIDWORKS returns an empty SafeArray or S\_false.

You must determine the number of points in the leader to use the data returned by this method. The number of points is a function of the number of segments in the leader. There can be one or two segments in a leader line, depending on whether or not it is a straight, bent, or underlined leader. Use [IAnnotation::GetLeaderStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderStyle.md)  
to determine the number of points in the leader.

- If IAnnotation::GetLeaderStyle returns swNO\_LEADER, then the number of points = 0.
- If IAnnotation::GetLeaderStyle returns swSTRAIGHT and swUNDERLINED then the number  
  of points = 2.
- If IAnnotation::GetLeaderStyle returns swBENT, then the number of points = 3.

Additionally, for the COM interface, you must determine the number of points to allocate the appropriate size array for the return value. The number of points must also be passed to the method to help prevent overwrite problems if you have not allocated an array that is the correct size. If the number of points passed does not match what is found, SOLIDWORKS does not return any point information and returns S\_false.

The format of the return array is:

> retval[0] = X-coordinate of first leader point
>
> retval[1] = Y-coordinate of first leader point
>
> retval[2] = Z-coordinate of first leader point

> retval[3] = X-coordinate of second leader point
>
> retval[4] = Y-coordinate of second leader point
>
> retval[5] = Z-coordinate of second leader point
>
> retval[6] = X-coordinate of third leader point
>
> retval[7] = Y-coordinate of third leader point
>
> retval[8] = Z-coordinate of third leader point

You cannot directly set the leader coordinate information. The leader coordinates are computed based on the annotations text and attachment points. Use [IAnnotation::GetPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPosition.md) and [IAnnotation::SetPosition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetPosition.md) to get and set the text point.

Example

[Get Display Dimensions, GTols, and Surface-finish Symbols (VBA)](Get_Display_Dimensions,_Gtols,_and_Surface-Finish_Symbols_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::GetDashedLeader Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetDashedLeader.md)  
[IAnnotation::GetLeaderAllAround Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderAllAround.md)  
[IAnnotation::GetLeaderPerpendicular Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderPerpendicular.md)  
[IAnnotation::GetLeaderSide Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderSide.md)  
[IAnnotation::GetMultiJogLeaderCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetMultiJogLeaderCount.md)  
[IAnnotation::GetMultiJogLeaders Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetMultiJogLeaders.md)  
[IAnnotation::IGetLeaderPointsAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetLeaderPointsAtIndex.md)  
[IAnnotation::SetLeader3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetLeader3.md)  
[IAnnotation::BentLeaderLength Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~BentLeaderLength.md)  
[IAnnotation::LeaderLineStyle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderLineStyle.md)  
[IAnnotation::LeaderThickness Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderThickness.md)  
[IAnnotation::LeaderThicknessCustom Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderThicknessCustom.md)  
[IAnnotation::UseDocDispLeader Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~UseDocDispLeader.md)  
[IAnnotation::SetLeaderAttachmentPointAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetLeaderAttachmentPointAtIndex.md)
