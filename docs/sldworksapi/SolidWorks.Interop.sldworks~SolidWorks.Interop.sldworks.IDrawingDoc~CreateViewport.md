# CreateViewport Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport`

Obsolete. Superseded by IDrawingDoc::CreateViewport3.
Obsolete. Superseded by [IDrawingDoc::CreateViewport3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateViewport( _
   ByVal LowerLeftX As System.Double, _
   ByVal LowerLeftY As System.Double, _
   ByVal UpperRightX As System.Double, _
   ByVal UpperRightY As System.Double, _
   ByVal SketchSize As System.Short _
) As System.String
```

```

Dim instance As IDrawingDoc
Dim LowerLeftX As System.Double
Dim LowerLeftY As System.Double
Dim UpperRightX As System.Double
Dim UpperRightY As System.Double
Dim SketchSize As System.Short
Dim value As System.String
 
value = instance.CreateViewport(LowerLeftX, LowerLeftY, UpperRightX, UpperRightY, SketchSize)
```

```

System.string CreateViewport( 
   System.double LowerLeftX,
   System.double LowerLeftY,
   System.double UpperRightX,
   System.double UpperRightY,
   System.short SketchSize
)
```

```

System.String^ CreateViewport( 
   System.double LowerLeftX,
   System.double LowerLeftY,
   System.double UpperRightX,
   System.double UpperRightY,
   System.short SketchSize
) 
```

#### Parameters

*LowerLeftX*

*LowerLeftY*

*UpperRightX*

*UpperRightY*

*SketchSize*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
