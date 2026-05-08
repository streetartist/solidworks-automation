# SyncFlexibleSubAssemblies Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData~SyncFlexibleSubAssemblies`

Gets or sets whether to synchronize the movement of mirrored components with the movement of seed components in the flexible subassembly.
Gets or sets whether to synchronize the movement of mirrored components with the movement of seed components in the flexible subassembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SyncFlexibleSubAssemblies As System.Boolean
```

```

Dim instance As IMirrorComponentFeatureData
Dim value As System.Boolean
 
instance.SyncFlexibleSubAssemblies = value
 
value = instance.SyncFlexibleSubAssemblies
```

```

System.bool SyncFlexibleSubAssemblies {get; set;}
```

```

property System.bool SyncFlexibleSubAssemblies {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to synchronize movements of mirrored and seed flexible subassembly components, false to not

Example

See the [IMirrorComponentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMirrorComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData.md)  
[IMirrorComponentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.md)
