# DecalID Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~DecalID`

Gets the SOLIDWORKS decal ID.
Gets the SOLIDWORKS decal ID.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property DecalID As System.Integer
```

```

Dim instance As IDecal
Dim value As System.Integer
 
value = instance.DecalID
```

```

System.int DecalID {get;}
```

```

property System.int DecalID {
   System.int get();
}
```

#### Property Value

SOLIDWORKS decal ID (index number)

Remarks

By default, decal IDs are persistent, which means if three decals (IDs 1, 2, and 3) were applied to the model, and you [removed decal](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteDecal.md) ID 2, then the remaining decal IDs are 1 and 3.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDecal Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal.md)  
[IDecal Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal_members.md)
