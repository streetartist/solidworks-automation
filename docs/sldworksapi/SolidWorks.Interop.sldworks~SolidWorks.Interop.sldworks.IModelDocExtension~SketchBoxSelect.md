# SketchBoxSelect Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SketchBoxSelect`

Box selects all of the entities in a sketch within the specified coordinates of the selection box.
Box selects all of the entities in a sketch within the specified coordinates of the selection box.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SketchBoxSelect( _
   ByVal FirstPtX As System.Double, _
   ByVal FirstPtY As System.Double, _
   ByVal FirstPtZ As System.Double, _
   ByVal SecondPtX As System.Double, _
   ByVal SecondPtY As System.Double, _
   ByVal SecondPtZ As System.Double _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim FirstPtX As System.Double
Dim FirstPtY As System.Double
Dim FirstPtZ As System.Double
Dim SecondPtX As System.Double
Dim SecondPtY As System.Double
Dim SecondPtZ As System.Double
Dim value As System.Boolean
 
value = instance.SketchBoxSelect(FirstPtX, FirstPtY, FirstPtZ, SecondPtX, SecondPtY, SecondPtZ)
```

```

System.bool SketchBoxSelect( 
   System.double FirstPtX,
   System.double FirstPtY,
   System.double FirstPtZ,
   System.double SecondPtX,
   System.double SecondPtY,
   System.double SecondPtZ
)
```

```

System.bool SketchBoxSelect( 
   System.double FirstPtX,
   System.double FirstPtY,
   System.double FirstPtZ,
   System.double SecondPtX,
   System.double SecondPtY,
   System.double SecondPtZ
) 
```

#### Parameters

*FirstPtX*
:   x coordinate of the first corner of the box

*FirstPtY*
:   y coordinate of the first corner of the box

*FirstPtZ*
:   z coordinate of the first corner of the box

*SecondPtX*
:   x coordinate of the opposite diagonal corner of the box

*SecondPtY*
:   y coordinate of the opposite diagonal corner of the box

*SecondPtZ*
:   z coordinate of the opposite diagonal corner of the box

#### Return Value

True if the sketch entities lying in the specified coordinates are box-selected, false if not

Example

[Box Select a Sketch (VB.NET)](Box_Select_a_Sketch_Example_VBNET.htm)  
[Box Select a Sketch (VBA)](Box_Select_a_Sketch_Example_VB.htm)  
[Box Select a Sketch (C#)](Box_Select_a_Sketch_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
