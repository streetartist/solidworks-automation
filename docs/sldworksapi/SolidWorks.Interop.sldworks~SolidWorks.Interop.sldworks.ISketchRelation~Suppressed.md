# Suppressed Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~Suppressed`

Gets or sets whether this relation is suppressed or not.
Gets or sets whether this relation is suppressed or not.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Suppressed As System.Boolean
```

```

Dim instance As ISketchRelation
Dim value As System.Boolean
 
instance.Suppressed = value
 
value = instance.Suppressed
```

```

System.bool Suppressed {get; set;}
```

```

property System.bool Suppressed {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True the relation is suppressed, false it is not

Example

[Replace Sketch Relation (VBA)](Replace_Sketch_Relation_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchRelation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.md)  
[ISketchRelation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation_members.md)
