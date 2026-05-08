# Lock Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Lock`

Gets or sets whether the configuration is locked.
Gets or sets whether the configuration is locked.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Lock As System.Boolean
```

```

Dim instance As IConfiguration
Dim value As System.Boolean
 
instance.Lock = value
 
value = instance.Lock
```

```

System.bool Lock {get; set;}
```

```

property System.bool Lock {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True for locked configuration, false for unlocked configuration

Remarks

The names of configurations should not contain any of the special characters reserved  
by SOLIDWORKS.

Example

[Change Configuration Properties (VBA)](Change_Configuration_Properties_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)
