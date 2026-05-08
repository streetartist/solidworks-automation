# IInsertMacroFeature Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IInsertMacroFeature`

Obsolete. Superseded by IFeatureManager::IInsertMacroFeature3.
Obsolete. Superseded by [IFeatureManager::IInsertMacroFeature3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertMacroFeature3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IInsertMacroFeature( _
   ByVal CmdFile As System.String, _
   ByVal CmdModule As System.String, _
   ByVal CmdProcedure As System.String, _
   ByVal ParamCount As System.Integer, _
   ByRef ParamNames As System.String, _
   ByRef ParamTypes As System.Integer, _
   ByRef ParamValues As System.String, _
   ByVal PmFile As System.String, _
   ByVal PmModule As System.String, _
   ByVal PmProcedure As System.String _
) As Feature
```

```

Dim instance As IModelDoc2
Dim CmdFile As System.String
Dim CmdModule As System.String
Dim CmdProcedure As System.String
Dim ParamCount As System.Integer
Dim ParamNames As System.String
Dim ParamTypes As System.Integer
Dim ParamValues As System.String
Dim PmFile As System.String
Dim PmModule As System.String
Dim PmProcedure As System.String
Dim value As Feature
 
value = instance.IInsertMacroFeature(CmdFile, CmdModule, CmdProcedure, ParamCount, ParamNames, ParamTypes, ParamValues, PmFile, PmModule, PmProcedure)
```

```

Feature IInsertMacroFeature( 
   System.string CmdFile,
   System.string CmdModule,
   System.string CmdProcedure,
   System.int ParamCount,
   ref System.string ParamNames,
   ref System.int ParamTypes,
   ref System.string ParamValues,
   System.string PmFile,
   System.string PmModule,
   System.string PmProcedure
)
```

```

Feature^ IInsertMacroFeature( 
   System.String^ CmdFile,
   System.String^ CmdModule,
   System.String^ CmdProcedure,
   System.int ParamCount,
   System.String^% ParamNames,
   System.int% ParamTypes,
   System.String^% ParamValues,
   System.String^ PmFile,
   System.String^ PmModule,
   System.String^ PmProcedure
) 
```

#### Parameters

*CmdFile*

*CmdModule*

*CmdProcedure*

*ParamCount*

*ParamNames*

*ParamTypes*

*ParamValues*

*PmFile*

*PmModule*

*PmProcedure*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
