# LockRotation Property (IConcentricMateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData~LockRotation`

Gets or sets whether to lock the rotation of the entities in this concentric mate.
Gets or sets whether to lock the rotation of the entities in this concentric mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LockRotation As System.Boolean
```

```

Dim instance As IConcentricMateFeatureData
Dim value As System.Boolean
 
instance.LockRotation = value
 
value = instance.LockRotation
```

```

System.bool LockRotation {get; set;}
```

```

property System.bool LockRotation {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to lock rotation, false to not

Example

See the [IConcentricMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConcentricMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData.md)  
[IConcentricMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData_members.md)
