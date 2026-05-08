# ForceSurfaceContact Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData~ForceSurfaceContact`

Gets or sets whether to join any coincident faces and any intruding volumes.
Gets or sets whether to join any coincident faces and any intruding volumes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ForceSurfaceContact As System.Boolean
```

```

Dim instance As IJoinFeatureData
Dim value As System.Boolean
 
instance.ForceSurfaceContact = value
 
value = instance.ForceSurfaceContact
```

```

System.bool ForceSurfaceContact {get; set;}
```

```

property System.bool ForceSurfaceContact {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to join any coincident faces and any intruding volumes, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IJoinFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData.md)  
[IJoinFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData_members.md)
