# Layer Property (ISketchBlockInstance)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Layer`

Gets or sets the name of the layer where this block is located.
Gets or sets the name of the layer where this block is located.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Layer As System.String
```

```

Dim instance As ISketchBlockInstance
Dim value As System.String
 
instance.Layer = value
 
value = instance.Layer
```

```

System.string Layer {get; set;}
```

```

property System.String^ Layer {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Name of layer

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md)  
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.md)
