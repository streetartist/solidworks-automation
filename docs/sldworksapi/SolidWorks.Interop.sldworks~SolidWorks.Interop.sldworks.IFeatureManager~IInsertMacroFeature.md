# IInsertMacroFeature Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertMacroFeature`

Obsolete. Superseded by IFeatureManager::IInsertMacroFeature3.
Obsolete. Superseded by [IFeatureManager::IInsertMacroFeature3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertMacroFeature3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IInsertMacroFeature( _
   ByVal BaseName As System.String, _
   ByVal ProgId As System.String, _
   ByRef MacroMethods As System.String, _
   ByVal ParamCount As System.Integer, _
   ByRef ParamNames As System.String, _
   ByRef ParamTypes As System.Integer, _
   ByRef ParamValues As System.String, _
   ByVal EditBody As Body2, _
   ByVal Options As System.Integer _
) As Feature
```

```

Dim instance As IFeatureManager
Dim BaseName As System.String
Dim ProgId As System.String
Dim MacroMethods As System.String
Dim ParamCount As System.Integer
Dim ParamNames As System.String
Dim ParamTypes As System.Integer
Dim ParamValues As System.String
Dim EditBody As Body2
Dim Options As System.Integer
Dim value As Feature
 
value = instance.IInsertMacroFeature(BaseName, ProgId, MacroMethods, ParamCount, ParamNames, ParamTypes, ParamValues, EditBody, Options)
```

```

Feature IInsertMacroFeature( 
   System.string BaseName,
   System.string ProgId,
   ref System.string MacroMethods,
   System.int ParamCount,
   ref System.string ParamNames,
   ref System.int ParamTypes,
   ref System.string ParamValues,
   Body2 EditBody,
   System.int Options
)
```

```

Feature^ IInsertMacroFeature( 
   System.String^ BaseName,
   System.String^ ProgId,
   System.String^% MacroMethods,
   System.int ParamCount,
   System.String^% ParamNames,
   System.int% ParamTypes,
   System.String^% ParamValues,
   Body2^ EditBody,
   System.int Options
) 
```

#### Parameters

*BaseName*

*ProgId*

*MacroMethods*

*ParamCount*

*ParamNames*

*ParamTypes*

*ParamValues*

*EditBody*

*Options*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
