# GetArrowHeadSizeAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadSizeAtIndex`

Gets the arrow head size of the specified leader on this annotation.
Gets the arrow head size of the specified leader on this annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetArrowHeadSizeAtIndex( _
   ByVal Index As System.Integer, _
   ByRef UseDoc As System.Boolean, _
   ByRef Length As System.Double, _
   ByRef Width As System.Double, _
   ByRef Height As System.Double _
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
 
value = instance.GetArrowHeadSizeAtIndex(Index, UseDoc, Length, Width, Height)
```

```

System.bool GetArrowHeadSizeAtIndex( 
   System.int Index,
   out System.bool UseDoc,
   out System.double Length,
   out System.double Width,
   out System.double Height
)
```

```

System.bool GetArrowHeadSizeAtIndex( 
   System.int Index,
   [Out] System.bool UseDoc,
   [Out] System.double Length,
   [Out] System.double Width,
   [Out] System.double Height
) 
```

#### Parameters

*Index*
:   Index of leader on this annotation

*UseDoc*
:   TRUE indicates that the document default setting for arrow head size was used, FALSE  
    indicates that the Length, Width, and Height values were specified

*Length*
:   Length of arrow head

*Width*
:   Width of arrow head

*Height*
:   Height of arrow head

#### Return Value

True if the method succeeds, false if not

Remarks

The index value is 0-based. Therefore, a valid index value is greater than or equal to 0, but less than the number of leaders on this annotation. Use [IAnnotation::GetArrowHeadCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadCount.md) to find the number of leaders on this annotation. If the index value is invalid, SOLIDWORKS returns the arrowhead style as -1, and returns an S\_FALSE status (COM interface).

Use [IAnnotation::SetArrowHeadSizeAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetArrowHeadSizeAtIndex.md) to set the arrow head size of a specific leader.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::GetArrowHeadStyleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetArrowHeadStyleAtIndex.md)  
[IAnnotation::SetArrowHeadStyleAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetArrowHeadStyleAtIndex.md)
