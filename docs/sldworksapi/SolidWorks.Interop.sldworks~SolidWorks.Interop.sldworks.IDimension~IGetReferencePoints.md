# IGetReferencePoints Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetReferencePoints`

Gets the reference points for this dimension.
Gets the reference points for this dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetReferencePoints( _
   ByVal PointsCount As System.Integer _
) As MathPoint
```

```

Dim instance As IDimension
Dim PointsCount As System.Integer
Dim value As MathPoint
 
value = instance.IGetReferencePoints(PointsCount)
```

```

MathPoint IGetReferencePoints( 
   System.int PointsCount
)
```

```

MathPoint^ IGetReferencePoints( 
   System.int PointsCount
) 
```

#### Parameters

*PointsCount*
:   Number of reference points for this dimension

#### Return Value

- in-process, unmanaged C++: Pointer to the [IMathPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) object

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Call [IDimension::IGetReferencePointsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetReferencePointsCount.md) before calling this method to determine the size of the array.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)  
[IDimension::ISetReferencePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetReferencePoints.md)  
[IDimension::ReferencePoints Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ReferencePoints.md)
