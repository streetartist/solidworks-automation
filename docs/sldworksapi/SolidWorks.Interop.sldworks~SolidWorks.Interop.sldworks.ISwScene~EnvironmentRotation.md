# EnvironmentRotation Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene~EnvironmentRotation`

Gets or sets the rotation of the environment image of this scene.
Gets or sets the rotation of the environment image of this scene.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EnvironmentRotation As System.Double
```

```

Dim instance As ISwScene
Dim value As System.Double
 
instance.EnvironmentRotation = value
 
value = instance.EnvironmentRotation
```

```

System.double EnvironmentRotation {get; set;}
```

```

property System.double EnvironmentRotation {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

0.0 <= Rotation in degrees <= 360.0

Example

See the [ISwScene](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISwScene Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene.md)  
[ISwScene Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.md)
