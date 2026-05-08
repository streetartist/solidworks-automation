# Owner Property (ICustomPropertyManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Owner`

Gets the owner of this custom property.
Gets the owner of this custom property.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Owner As System.Object
```

```

Dim instance As ICustomPropertyManager
Dim value As System.Object
 
value = instance.Owner
```

```

System.object Owner {get;}
```

```

property System.Object^ Owner {
   System.Object^ get();
}
```

#### Property Value

Pointer to owner of the custom property; currently either a [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) or a [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.md)  
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.md)
