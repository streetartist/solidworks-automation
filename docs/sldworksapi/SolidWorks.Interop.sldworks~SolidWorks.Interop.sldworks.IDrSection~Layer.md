# Layer Property (IDrSection)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~Layer`

Gets or sets the name of the layer on which the section line lies.
Gets or sets the name of the layer on which the section line lies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Layer As System.String
```

```

Dim instance As IDrSection
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

Layer name

Remarks

An empty string indicates no layer. If you set the layer to a layer name that does not exist, nothing happens.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md)  
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.md)  
[ILayer Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer.md)
