# InsertMacroFeature Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertMacroFeature`

Obsolete. Superseded by IFeatureManager::InsertMacroFeature3.
Obsolete. Superseded by [IFeatureManager::InsertMacroFeature3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMacroFeature3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertMacroFeature( _
   ByVal CmdFile As System.String, _
   ByVal CmdModule As System.String, _
   ByVal CmdProcedure As System.String, _
   ByVal ParamNames As System.Object, _
   ByVal ParamTypes As System.Object, _
   ByVal ParamValues As System.Object, _
   ByVal PmFile As System.String, _
   ByVal PmModule As System.String, _
   ByVal PmProcedure As System.String _
) As System.Object
```

```

Dim instance As IModelDoc2
Dim CmdFile As System.String
Dim CmdModule As System.String
Dim CmdProcedure As System.String
Dim ParamNames As System.Object
Dim ParamTypes As System.Object
Dim ParamValues As System.Object
Dim PmFile As System.String
Dim PmModule As System.String
Dim PmProcedure As System.String
Dim value As System.Object
 
value = instance.InsertMacroFeature(CmdFile, CmdModule, CmdProcedure, ParamNames, ParamTypes, ParamValues, PmFile, PmModule, PmProcedure)
```

```

System.object InsertMacroFeature( 
   System.string CmdFile,
   System.string CmdModule,
   System.string CmdProcedure,
   System.object ParamNames,
   System.object ParamTypes,
   System.object ParamValues,
   System.string PmFile,
   System.string PmModule,
   System.string PmProcedure
)
```

```

System.Object^ InsertMacroFeature( 
   System.String^ CmdFile,
   System.String^ CmdModule,
   System.String^ CmdProcedure,
   System.Object^ ParamNames,
   System.Object^ ParamTypes,
   System.Object^ ParamValues,
   System.String^ PmFile,
   System.String^ PmModule,
   System.String^ PmProcedure
) 
```

#### Parameters

*CmdFile*

*CmdModule*

*CmdProcedure*

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
