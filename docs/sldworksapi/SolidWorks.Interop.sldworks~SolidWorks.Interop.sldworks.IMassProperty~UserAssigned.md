# UserAssigned Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~UserAssigned`

Gets whether the mass property values are user-defined or calculated for this document, regardless of which model is being edited.
Gets whether the mass property values are user-defined or calculated for this document, regardless of which model is being edited.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UserAssigned As System.Boolean
```

```

Dim instance As IMassProperty
Dim value As System.Boolean
 
instance.UserAssigned = value
 
value = instance.UserAssigned
```

```

System.bool UserAssigned {get; set;}
```

```

property System.bool UserAssigned {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if mass property values are user-defined, false if calculated

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.md)  
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.md)  
[IMassProperty::ISetAssignedMassProp Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetAssignedMassProp.md)  
[IMassProperty::SetAssignedMassProp Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetAssignedMassProp.md)
