# SetLeader3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetLeader3`

Sets the leader characteristics for this annotation.
Sets the leader characteristics for this annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetLeader3( _
   ByVal LeaderStyle As System.Integer, _
   ByVal LeaderSide As System.Integer, _
   ByVal SmartArrowHeadStyle As System.Boolean, _
   ByVal Perpendicular As System.Boolean, _
   ByVal AllAround As System.Boolean, _
   ByVal Dashed As System.Boolean _
) As System.Integer
```

```

Dim instance As IAnnotation
Dim LeaderStyle As System.Integer
Dim LeaderSide As System.Integer
Dim SmartArrowHeadStyle As System.Boolean
Dim Perpendicular As System.Boolean
Dim AllAround As System.Boolean
Dim Dashed As System.Boolean
Dim value As System.Integer
 
value = instance.SetLeader3(LeaderStyle, LeaderSide, SmartArrowHeadStyle, Perpendicular, AllAround, Dashed)
```

```

System.int SetLeader3( 
   System.int LeaderStyle,
   System.int LeaderSide,
   System.bool SmartArrowHeadStyle,
   System.bool Perpendicular,
   System.bool AllAround,
   System.bool Dashed
)
```

```

System.int SetLeader3( 
   System.int LeaderStyle,
   System.int LeaderSide,
   System.bool SmartArrowHeadStyle,
   System.bool Perpendicular,
   System.bool AllAround,
   System.bool Dashed
) 
```

#### Parameters

*LeaderStyle*
:   Leader style as defined in [swLeaderStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLeaderStyle_e.html) (see **Remarks**)

*LeaderSide*
:   Leader side as defined in [swLeaderSide\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLeaderSide_e.html) (see **Remarks**)

*SmartArrowHeadStyle*
:   True to enable smart arrowhead style, false to disable it (see **Remarks**)

*Perpendicular*
:   True to enable perpendicular bent leader display, false to disable it (see **Remarks**)

*AllAround*
:   True to enable all around (weld, surface finish, or Gtol) symbol display, false to disable it (see **Remarks**)

*Dashed*
:   True to enable dashed line leader display; false to enable solid-line leader (see **Remarks**)

#### Return Value

Indicates whether the operation was successful (see **Remarks**)

Remarks

Not all annotations support all styles of leaders or leader characteristics. Only notes, GTols, surface finish symbols, weld symbols, datum target symbols, and block instances support leaders of any kind.

- Weld symbol leaders can be hidden, but are always bent; straight leaders (swSTRAIGHT) are not supported.
- Datum target symbols can have straight or bent leaders, but cannot be hidden (swNO\_LEADER is not supported).
- Only notes support underline leaders (swUNDERLINED).
- GTols are the only type of annotation that supports perpendicular bent leaders.
- GTols and weld symbols are the only types of annotations that support all around leader symbols.
- Datum target symbols are the only type of annotation that supports dashed leaders.

This method sets the characteristics of the annotation, not the individual leaders. You can get or set these characteristics whether leaders are displayed.

|  |  |
| --- | --- |
| **Use...** | **To...** |
| [IAnnotation::GetDashedLeader](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetDashedLeader.md) | Determine whether this leader is a dashed line or a solid line. |
| [IAnnotation::GetLeaderAllARound](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderAllAround.md) | Determine whether all around symbol display is enabled or disabled. |
| [IAnnotation::GetLeaderPerpendicular](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderPerpendicular.md) | Determine whether perpendicular bent leader display is enabled or disabled. |
| [IAnnotation::GetLeaderSide](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderSide.md) | Get the leader attachment side setting. |
| [IAnnotation::GetLeaderStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderStyle.md) | Get style of leader (hidden, straight, bent, or underline). |
| [IAnnotation::GetSmartArrowHeadStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetSmartArrowHeadStyle.md) | Determine whether smart arrowhead style is enabled or disabled. |

You can set the leader side, smart arrowhead style, and bent leader values at any time. However, if leader display is disabled, you cannot affect the display of the annotation by setting these values. You can also set the perpendicular bent leader and all around symbol display at any time, but if bent leaders are disabled, you cannot affect the display of the annotation by setting these values.

The return status of this operation can have the following values:

- 0 = Leader characteristics were successfully set
- -1 = Leader characteristics were not set because of an unknown error
- -2 = Leader attachment side setting is invalid
- -3 = Leaders are not supported on this type of annotation
- -4 = Leaders cannot be disabled on this type of annotation
- -5 = Bent leaders cannot be disabled on this type of annotation
- -6 = Underline style leaders are not allowed on this type of annotation

If leader display is enabled, then this method changes the visible model.

Example

[Insert GTol (C#)](Insert_GTol_Example_CSharp.htm)  
[Insert GTol (VB.NET)](Insert_GTol_Example_VBNET.htm)  
[Insert GTol (VBA)](Insert_GTol_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::GetLeader Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeader.md)  
[IAnnotation::GetLeaderCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderCount.md)  
[IAnnotation::GetLeaderPointsAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderPointsAtIndex.md)  
[IAnnotation::GetMultiJogLeaderCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetMultiJogLeaderCount.md)  
[IAnnotation::GetMultiJogLeaders Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetMultiJogLeaders.md)  
[IAnnotation::BentLeaderLength Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~BentLeaderLength.md)  
[IAnnotation::LeaderLineStyle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderLineStyle.md)  
[IAnnotation::LeaderThickness Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderThickness.md)  
[IAnnotation::LeaderThicknessCustom Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LeaderThicknessCustom.md)  
[IAnnotation::UseDocDispLeader Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~UseDocDispLeader.md)  
[IAnnotation::SetLeaderAttachmentPointAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetLeaderAttachmentPointAtIndex.md)
