# InsertCircularNotePattern Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertCircularNotePattern`

Inserts a circular note pattern using the selected note.
Inserts a circular note pattern using the selected [note](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertCircularNotePattern( _
   ByVal ArcRadius As System.Double, _
   ByVal ArcAngle As System.Double, _
   ByVal PatternNum As System.Integer, _
   ByVal PatternSpacing As System.Double, _
   ByVal PatternRotate As System.Boolean, _
   ByVal DeleteInstances As System.String _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim ArcRadius As System.Double
Dim ArcAngle As System.Double
Dim PatternNum As System.Integer
Dim PatternSpacing As System.Double
Dim PatternRotate As System.Boolean
Dim DeleteInstances As System.String
Dim value As System.Boolean
 
value = instance.InsertCircularNotePattern(ArcRadius, ArcAngle, PatternNum, PatternSpacing, PatternRotate, DeleteInstances)
```

```

System.bool InsertCircularNotePattern( 
   System.double ArcRadius,
   System.double ArcAngle,
   System.int PatternNum,
   System.double PatternSpacing,
   System.bool PatternRotate,
   System.string DeleteInstances
)
```

```

System.bool InsertCircularNotePattern( 
   System.double ArcRadius,
   System.double ArcAngle,
   System.int PatternNum,
   System.double PatternSpacing,
   System.bool PatternRotate,
   System.String^ DeleteInstances
) 
```

#### Parameters

*ArcRadius*
:   Radius for the circular note pattern

*ArcAngle*
:   Angle relative to the notes being patterned

*PatternNum*
:   Total number of pattern instances, including the seed geometry

*PatternSpacing*
:   Spacing between pattern instances in radians

*PatternRotate*
:   True to rotate the pattern, false to not

*DeleteInstances*
:   Number of instances to delete, passed as a string formatted as "(a) (b) (c) "

#### Return Value

True if the circular note pattern is created, false if not

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
[IDrawingDoc::InsertLinearNotePattern Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~InsertLinearNotePattern.md)
