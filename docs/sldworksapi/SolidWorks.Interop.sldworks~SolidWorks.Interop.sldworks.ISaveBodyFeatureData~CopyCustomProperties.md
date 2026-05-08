# CopyCustomProperties Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData~CopyCustomProperties`

Gets or sets whether to copy custom properties to the new parts.
Gets or sets whether to copy custom properties to the new parts.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CopyCustomProperties As System.Boolean
```

```

Dim instance As ISaveBodyFeatureData
Dim value As System.Boolean
 
instance.CopyCustomProperties = value
 
value = instance.CopyCustomProperties
```

```

System.bool CopyCustomProperties {get; set;}
```

```

property System.bool CopyCustomProperties {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

See **Remarks**

Remarks

**For VBA, .NET:**

True to copy custom properties to the new parts, false to not.

**For C++:**

VARIANT\_TRUE (-1) to copy custom properties to the new parts, VARIANT\_FALSE (0) to not.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISaveBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData.md)  
[ISaveBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData_members.md)
