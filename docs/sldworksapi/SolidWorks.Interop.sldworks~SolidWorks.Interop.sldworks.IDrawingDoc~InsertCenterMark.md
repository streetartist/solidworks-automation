# InsertCenterMark Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertCenterMark`

Obsolete. Superseded by IDrawingDoc::InsertCenterMark2.
Obsolete. Superseded by [IDrawingDoc::InsertCenterMark2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertCenterMark2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertCenterMark( _
   ByVal UseDoc As System.Boolean, _
   ByVal Size As System.Double, _
   ByVal ShowLines As System.Boolean, _
   ByVal Angle As System.Double _
) As CenterMark
```

```

Dim instance As IDrawingDoc
Dim UseDoc As System.Boolean
Dim Size As System.Double
Dim ShowLines As System.Boolean
Dim Angle As System.Double
Dim value As CenterMark
 
value = instance.InsertCenterMark(UseDoc, Size, ShowLines, Angle)
```

```

CenterMark InsertCenterMark( 
   System.bool UseDoc,
   System.double Size,
   System.bool ShowLines,
   System.double Angle
)
```

```

CenterMark^ InsertCenterMark( 
   System.bool UseDoc,
   System.double Size,
   System.bool ShowLines,
   System.double Angle
) 
```

#### Parameters

*UseDoc*

*Size*

*ShowLines*

*Angle*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
