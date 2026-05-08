# EnvironmentSize Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~EnvironmentSize`

Gets or sets the size of the high dynamic range imaging (HDRI) scene sphere that surrounds the model.
Gets or sets the size of the high dynamic range imaging (HDRI) scene sphere that surrounds the model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EnvironmentSize As System.Double
```

```

Dim instance As ISwScene
Dim value As System.Double
 
instance.EnvironmentSize = value
 
value = instance.EnvironmentSize
```

```

System.double EnvironmentSize {get; set;}
```

```

property System.double EnvironmentSize {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Size of the HDRI scene sphere

Remarks

This property is valid only if [ISwScene::FlattenFloor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~FlattenFloor.md) is set to true.

Example

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md)  
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.md)
