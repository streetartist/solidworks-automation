# DimXpertManager Property (IConfiguration)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~DimXpertManager`

Gets the DimXpert schema for this configuration.
Gets the DimXpert schema for this configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property DimXpertManager( _
   ByVal CreateSchema As System.Boolean _
) As DimXpertManager
```

```

Dim instance As IConfiguration
Dim CreateSchema As System.Boolean
Dim value As DimXpertManager
 
value = instance.DimXpertManager(CreateSchema)
```

```

DimXpertManager DimXpertManager( 
   System.bool CreateSchema
) {get;}
```

```

property DimXpertManager^ DimXpertManager {
   DimXpertManager^ get(System.bool CreateSchema);
}
```

#### Parameters

*CreateSchema*
:   True to create DimXpert schema if it does not already exist; false otherwise

#### Property Value

Pointer to [IDimXpertManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager.md) object

Remarks

This interface retrieves the DimXpert schema information for opened parts which can be accessed in SOLIDWORKS via either the DimXpertManager tab of the Management Panel or the DimXpert tab of the CommandManager.

Example

[Get DimXpertManager Info (VBA)](Get_DimXpertManager_Info_Example_VB.htm)  
[Get DimXpertManager Info (VB.NET)](Get_DimXpertManager_Info_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)
