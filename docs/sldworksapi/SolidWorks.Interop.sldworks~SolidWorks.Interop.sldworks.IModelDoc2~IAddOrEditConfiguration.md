# IAddOrEditConfiguration Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IAddOrEditConfiguration`

Obsolete. Superseded by IConfiguraiton::GetParameters, IConfiguration::IGetParameters, IConfiguration::ISetParameters, and IConfiguration::SetParameters.
Obsolete. Superseded by [IConfiguraiton::GetParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParameters.md), [IConfiguration::IGetParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetParameters.md), [IConfiguration::ISetParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ISetParameters.md), and [IConfiguration::SetParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetParameters.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IAddOrEditConfiguration( _
   ByVal ConfigName As System.String, _
   ByVal ParamCount As System.Integer, _
   ByRef ParamNames As System.String, _
   ByRef ParamValues As System.String _
) As System.Integer
```

```

Dim instance As IModelDoc2
Dim ConfigName As System.String
Dim ParamCount As System.Integer
Dim ParamNames As System.String
Dim ParamValues As System.String
Dim value As System.Integer
 
value = instance.IAddOrEditConfiguration(ConfigName, ParamCount, ParamNames, ParamValues)
```

```

System.int IAddOrEditConfiguration( 
   System.string ConfigName,
   System.int ParamCount,
   ref System.string ParamNames,
   ref System.string ParamValues
)
```

```

System.int IAddOrEditConfiguration( 
   System.String^ ConfigName,
   System.int ParamCount,
   System.String^% ParamNames,
   System.String^% ParamValues
) 
```

#### Parameters

*ConfigName*

*ParamCount*

*ParamNames*

*ParamValues*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
