# GetRelationType Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~GetRelationType`

Gets the type of sketch relation.
Gets the type of sketch relation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetRelationType() As System.Integer
```

```

Dim instance As ISketchRelation
Dim value As System.Integer
 
value = instance.GetRelationType()
```

```

System.int GetRelationType()
```

```

System.int GetRelationType(); 
```

#### Return Value

Type of sketch relation as defined in [swConstraintType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConstraintType_e.html)

Example

[Get All Sketch Relations and Their Types (VBA)](Get_All_Sketch_Relations_and_Their_Types_Example_VB.htm)  
[Replace Sketch Relation (VBA)](Replace_Sketch_Relation_Example_VB.htm)  
[Get Sketch Relations (VBA)](Get_Sketch_Relations_Example_VB.htm)  
[Get Sketch Relations (VB.NET)](Get_Sketch_Relations_Example_VBNET.htm)  
[Get Sketch Relations (C#)](Get_Sketch_Relations_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchRelation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.md)  
[ISketchRelation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation_members.md)
