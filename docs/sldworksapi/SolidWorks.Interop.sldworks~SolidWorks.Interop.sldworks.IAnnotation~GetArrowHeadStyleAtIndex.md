# GetArrowHeadStyleAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadStyleAtIndex`

Gets the arrow head style of a specific leader on this annotation.
Gets the arrow head style of a specific leader on this annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetArrowHeadStyleAtIndex( _
   ByVal Index As System.Integer _
) As System.Integer
```

```

Dim instance As IAnnotation
Dim Index As System.Integer
Dim value As System.Integer
 
value = instance.GetArrowHeadStyleAtIndex(Index)
```

```

System.int GetArrowHeadStyleAtIndex( 
   System.int Index
)
```

```

System.int GetArrowHeadStyleAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index of leader within this annotation (see **Remarks**)

#### Return Value

Arrowhead style as defined in [swArrowStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

Remarks

The index value is 0-based. Therefore, a valid index value is greater than or equal to 0, but less than the number of leaders on this annotation. Use [IAnnotation::GetArrowHeadCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadCount.md) to find the number of leaders on this annotation. If the index value is invalid, SOLIDWORKS returns the arrowhead style as -1, and returns an S\_FALSE status (COM interface).

Use [IAnnotation::SetArrowHeadStyleAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetArrowHeadStyleAtIndex.md) to set the arrow head style of a specific leader.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::SetArrowHeadStyleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetArrowHeadStyleAtIndex.md)
