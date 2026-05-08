# HorizonHeight Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~HorizonHeight`

Gets or sets the height on the high dynamic range imaging (HDRI) scene sphere where the scene floor starts to flatten.
Gets or sets the height on the high dynamic range imaging (HDRI) scene sphere where the scene floor starts to flatten.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property HorizonHeight As System.Double
```

```

Dim instance As ISwScene
Dim value As System.Double
 
instance.HorizonHeight = value
 
value = instance.HorizonHeight
```

```

System.double HorizonHeight {get; set;}
```

```

property System.double HorizonHeight {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

0.0 <= Horizon height <= 1.0

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
