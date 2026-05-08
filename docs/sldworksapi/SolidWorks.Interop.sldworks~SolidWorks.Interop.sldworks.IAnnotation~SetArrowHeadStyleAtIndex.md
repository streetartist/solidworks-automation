# SetArrowHeadStyleAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetArrowHeadStyleAtIndex`

Sets the arrow head style of a specific leader on this annotation.
Sets the arrow head style of a specific leader on this annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetArrowHeadStyleAtIndex( _
   ByVal Index As System.Integer, _
   ByVal ArrowHeadStyle As System.Integer _
) As System.Integer
```

```

Dim instance As IAnnotation
Dim Index As System.Integer
Dim ArrowHeadStyle As System.Integer
Dim value As System.Integer
 
value = instance.SetArrowHeadStyleAtIndex(Index, ArrowHeadStyle)
```

```

System.int SetArrowHeadStyleAtIndex( 
   System.int Index,
   System.int ArrowHeadStyle
)
```

```

System.int SetArrowHeadStyleAtIndex( 
   System.int Index,
   System.int ArrowHeadStyle
) 
```

#### Parameters

*Index*
:   0-based index of leader within this annotation (see **Remarks**)

*ArrowHeadStyle*
:   Arrowhead style as defined in [swArrowStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

#### Return Value

Return status (see **Remarks**)

Remarks

A valid index value is greater than or equal to 0, but less than the number of leaders on this annotation. Use [IAnnotation::GetArrowHeadCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadCount.md) to find out how many leaders are on this annotation. An index value of -1 is also valid, and indicates that this arrowhead style should be applied to all leaders on this annotation. If the index value is  
invalid, SOLIDWORKS returns a retval of -2.

If smart arrowhead style is enabled on this annotation, then this method cannot change  
the arrowhead style of individual leaders, and retval is -3. Use [IAnnotation::GetSmartArrowHeadStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetSmartArrowHeadStyle.md) to determine if this flag is enabled or disabled.

The return status of this method can have the following values:

|  |  |
| --- | --- |
| **If value equals...** | **Then the arrowhead style was...** |
| 0 | Successfully set |
| -1 | Not set because of an unknown error |
| -2 | Not set because of an invalid index value |
| -3 | Not set because of smart arrowhead styles being enabled |
| -4 | Not set because of an invalid arrowhead style value |

If leader display is enabled, then this method changes the visible model. To see those  
changes, use [IModelDoc2::GraphicsRedraw2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GraphicsRedraw2.md) to reddraw the graphics window.

Use [IAnnotation::GetArrowHeadStyleAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadStyleAtIndex.md) to get the arrow head style of a specific leader.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::SetArrowHeadSizeAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetArrowHeadSizeAtIndex.md)  
[IAnnotation::GetArrowHeadSizeAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadSizeAtIndex.md)  
[IAnnotation::GetArrowHeadStyleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadStyleAtIndex.md)  
[IAnnotation::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadCount.md)
