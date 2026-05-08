# SetArrowHeadSizeAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetArrowHeadSizeAtIndex`

Sets the size of the arrow head of the specified leader on this annotation.
Sets the size of the arrow head of the specified leader on this annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetArrowHeadSizeAtIndex( _
   ByVal Index As System.Integer, _
   ByVal UseDoc As System.Boolean, _
   ByVal Length As System.Double, _
   ByVal Width As System.Double, _
   ByVal Height As System.Double _
) As System.Boolean
```

```

Dim instance As IAnnotation
Dim Index As System.Integer
Dim UseDoc As System.Boolean
Dim Length As System.Double
Dim Width As System.Double
Dim Height As System.Double
Dim value As System.Boolean
 
value = instance.SetArrowHeadSizeAtIndex(Index, UseDoc, Length, Width, Height)
```

```

System.bool SetArrowHeadSizeAtIndex( 
   System.int Index,
   System.bool UseDoc,
   System.double Length,
   System.double Width,
   System.double Height
)
```

```

System.bool SetArrowHeadSizeAtIndex( 
   System.int Index,
   System.bool UseDoc,
   System.double Length,
   System.double Width,
   System.double Height
) 
```

#### Parameters

*Index*
:   0-based index of leader on this annotation

*UseDoc*
:   True to use the document default setting for arrow head size, false to use the specified Length, Width, and Height values

*Length*
:   Length of leader on this annotation

*Width*
:   Width of leader on this annotation

*Height*
:   Height of leader on this annotation

Remarks

Use [IAnnotation::GetArrowHeadSizeAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadSizeAtIndex.md) to get the arrow head size of a specific leader.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadCount.md)  
[IAnnotation::GetArrowHeadStyleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadStyleAtIndex.md)  
[IAnnotation::SetArrowHeadStyleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetArrowHeadStyleAtIndex.md)
