# AddOrEditConfiguration Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddOrEditConfiguration`

Obsolete. Superseded by IConfiguraiton::GetParameters, IConfiguration::IGetParameters, IConfiguration::ISetParameters, and IConfiguration::SetParameters.
Obsolete. Superseded by [IConfiguraiton::GetParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameters.md), [IConfiguration::IGetParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetParameters.md), [IConfiguration::ISetParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ISetParameters.md), and [IConfiguration::SetParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetParameters.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddOrEditConfiguration( _
   ByVal ConfigName As System.String, _
   ByVal Params As System.Object, _
   ByVal Values As System.Object _
) As System.Integer
```

```

Dim instance As IModelDoc2
Dim ConfigName As System.String
Dim Params As System.Object
Dim Values As System.Object
Dim value As System.Integer
 
value = instance.AddOrEditConfiguration(ConfigName, Params, Values)
```

```

System.int AddOrEditConfiguration( 
   System.string ConfigName,
   System.object Params,
   System.object Values
)
```

```

System.int AddOrEditConfiguration( 
   System.String^ ConfigName,
   System.Object^ Params,
   System.Object^ Values
) 
```

#### Parameters

*ConfigName*

*Params*

*Values*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
