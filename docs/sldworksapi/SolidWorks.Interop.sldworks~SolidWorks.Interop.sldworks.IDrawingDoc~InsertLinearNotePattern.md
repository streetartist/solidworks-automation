# InsertLinearNotePattern Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertLinearNotePattern`

Inserts a linear note pattern using the selected note.
Inserts a linear note pattern using the selected [note](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertLinearNotePattern( _
   ByVal NumX As System.Integer, _
   ByVal NumY As System.Integer, _
   ByVal SpacingX As System.Double, _
   ByVal SpacingY As System.Double, _
   ByVal AngleX As System.Double, _
   ByVal AngleY As System.Double, _
   ByVal DeleteInstances As System.String _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim NumX As System.Integer
Dim NumY As System.Integer
Dim SpacingX As System.Double
Dim SpacingY As System.Double
Dim AngleX As System.Double
Dim AngleY As System.Double
Dim DeleteInstances As System.String
Dim value As System.Boolean
 
value = instance.InsertLinearNotePattern(NumX, NumY, SpacingX, SpacingY, AngleX, AngleY, DeleteInstances)
```

```

System.bool InsertLinearNotePattern( 
   System.int NumX,
   System.int NumY,
   System.double SpacingX,
   System.double SpacingY,
   System.double AngleX,
   System.double AngleY,
   System.string DeleteInstances
)
```

```

System.bool InsertLinearNotePattern( 
   System.int NumX,
   System.int NumY,
   System.double SpacingX,
   System.double SpacingY,
   System.double AngleX,
   System.double AngleY,
   System.String^ DeleteInstances
) 
```

#### Parameters

*NumX*
:   Total number of instances along the x axis, including the seed

*NumY*
:   Total number of instances along the y axis, including the seed

*SpacingX*
:   Spacing between pattern instances along the x axis

*SpacingY*
:   Spacing between pattern instances along the y axis

*AngleX*
:   Angle for direction 1 relative to the x axis

*AngleY*
:   Angle for direction 2 relative to the y axis

*DeleteInstances*
:   Number of instances to delete, passed as a string in the format "(a) (b) (c) "

#### Return Value

True if the linear note pattern is created, false if not

Example

[Insert Linear and Circular Note Patterns (C#)](Insert_Linear_and_Circular_Note_Patterns_Example_CSharp.htm)  
[Insert Linear and Circular Note Patterns (VB.NET)](Insert_Linear_and_Circular_Note_Patterns_Example_VBNET.htm)  
[Insert Linear and Circular Note Patterns (VBA)](Insert_Linear_and_Circular_Note_Patterns_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)  
[IDrawingDoc::InsertCircularNotePattern Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertCircularNotePattern.md)
