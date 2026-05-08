# LinkAll Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~LinkAll`

Gets or sets whether to link or unlink all custom properties to or from their parent parts.
Gets or sets whether to link or unlink all custom properties to or from their parent parts.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LinkAll As System.Boolean
```

```

Dim instance As ICustomPropertyManager
Dim value As System.Boolean
 
instance.LinkAll = value
 
value = instance.LinkAll
```

```

System.bool LinkAll {get; set;}
```

```

property System.bool LinkAll {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to link all custom properties, false to unlink all

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.md)  
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.md)  
[ICustomPropertyManager::LinkProperty Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~LinkProperty.md)
