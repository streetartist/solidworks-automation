# GetID Method (IConfiguration)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetID`

Gets the configuration ID of this configuration.
Gets the configuration ID of this configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetID() As System.Integer
```

```

Dim instance As IConfiguration
Dim value As System.Integer
 
value = instance.GetID()
```

```

System.int GetID()
```

```

System.int GetID(); 
```

#### Return Value

Configuration ID of this configuration

Remarks

A configuration ID:

- is unique within the document.
- is persistent across SOLIDWORKS sessions and never changes, even if you [change the name of the configuration](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Name.md).
- can be used to identify a specific configuration when multiple configurations exist in a model.
- cannot be assigned by users.
- is not the same as a [persistent reference ID](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm). You can get a configuration using its persistent reference ID, but you cannot get a configuration using this method.

Example

[Get ID of Active Configuration or Current Drawing Sheet (VB.NET)](Get_ID_of_Active_Configuration_or_Current_Drawing_Sheet_Example_VBNET.htm)  
[GEt ID of Active Configuration or Current Drawing Sheet (VBA)](Get_ID_of_Active_Configuration_or_Current_Drawing_Sheet_Example_VB.htm)  
[Get ID of Active Configuration or Current Drawing Sheet (C#)](Get_ID_of_Active_Configuration_or_Current_Drawing_Sheet_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.md)  
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.md)
