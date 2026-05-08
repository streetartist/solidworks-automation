# Definition Property (ISketchBlockInstance)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Definition`

Gets or sets the block definition for this block instance.
Gets or sets the block definition for this block instance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Definition As SketchBlockDefinition
```

```

Dim instance As ISketchBlockInstance
Dim value As SketchBlockDefinition
 
instance.Definition = value
 
value = instance.Definition
```

```

SketchBlockDefinition Definition {get; set;}
```

```

property SketchBlockDefinition^ Definition {
   SketchBlockDefinition^ get();
   void set (    SketchBlockDefinition^ value);
}
```

#### Property Value

[Block definition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md) for this block instance

Example

[Get Block Instance in Part or Assembly (VBA)](Get_Block_Instance_in_Part_or_Assembly_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md)  
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.md)
