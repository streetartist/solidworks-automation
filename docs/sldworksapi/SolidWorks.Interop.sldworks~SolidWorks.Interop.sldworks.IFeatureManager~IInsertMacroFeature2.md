# IInsertMacroFeature2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertMacroFeature2`

Obsolete. Superseded by IFeatureManager::IInsertMacroFeature3.
Obsolete. Superseded by [IFeatureManager::IInsertMacroFeature3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertMacroFeature3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IInsertMacroFeature2( _
   ByVal BaseName As System.String, _
   ByVal ProgId As System.String, _
   ByRef MacroMethods As System.String, _
   ByVal ParamCount As System.Integer, _
   ByRef ParamNames As System.String, _
   ByRef ParamTypes As System.Integer, _
   ByRef ParamValues As System.String, _
   ByVal DimCount As System.Integer, _
   ByRef DimTypes As System.Integer, _
   ByRef DimCountValues As System.Double, _
   ByVal EditBody As Body2, _
   ByVal IconCount As System.Integer, _
   ByRef IconFiles As System.String, _
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
Dim DimCount As System.Integer
Dim DimTypes As System.Integer
Dim DimCountValues As System.Double
Dim EditBody As Body2
Dim IconCount As System.Integer
Dim IconFiles As System.String
Dim Options As System.Integer
Dim value As Feature
 
value = instance.IInsertMacroFeature2(BaseName, ProgId, MacroMethods, ParamCount, ParamNames, ParamTypes, ParamValues, DimCount, DimTypes, DimCountValues, EditBody, IconCount, IconFiles, Options)
```

```

Feature IInsertMacroFeature2( 
   System.string BaseName,
   System.string ProgId,
   ref System.string MacroMethods,
   System.int ParamCount,
   ref System.string ParamNames,
   ref System.int ParamTypes,
   ref System.string ParamValues,
   System.int DimCount,
   ref System.int DimTypes,
   ref System.double DimCountValues,
   Body2 EditBody,
   System.int IconCount,
   ref System.string IconFiles,
   System.int Options
)
```

```

Feature^ IInsertMacroFeature2( 
   System.String^ BaseName,
   System.String^ ProgId,
   System.String^% MacroMethods,
   System.int ParamCount,
   System.String^% ParamNames,
   System.int% ParamTypes,
   System.String^% ParamValues,
   System.int DimCount,
   System.int% DimTypes,
   System.double% DimCountValues,
   Body2^ EditBody,
   System.int IconCount,
   System.String^% IconFiles,
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

*DimCount*

*DimTypes*

*DimCountValues*

*EditBody*

*IconCount*

*IconFiles*

*Options*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
