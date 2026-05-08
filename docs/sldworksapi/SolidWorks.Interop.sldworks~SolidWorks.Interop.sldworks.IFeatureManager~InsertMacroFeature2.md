# InsertMacroFeature2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMacroFeature2`

Obsolete. Superseded by IFeatureManager::InsertMacroFeature3.
Obsolete. Superseded by [IFeatureManager::InsertMacroFeature3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMacroFeature3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertMacroFeature2( _
   ByVal BaseName As System.String, _
   ByVal ProgId As System.String, _
   ByVal MacroMethods As System.Object, _
   ByVal ParamNames As System.Object, _
   ByVal ParamTypes As System.Object, _
   ByVal ParamValues As System.Object, _
   ByVal DimTypes As System.Object, _
   ByVal DimValues As System.Object, _
   ByVal EditBody As Body2, _
   ByVal IconFiles As System.Object, _
   ByVal Options As System.Integer _
) As Feature
```

```

Dim instance As IFeatureManager
Dim BaseName As System.String
Dim ProgId As System.String
Dim MacroMethods As System.Object
Dim ParamNames As System.Object
Dim ParamTypes As System.Object
Dim ParamValues As System.Object
Dim DimTypes As System.Object
Dim DimValues As System.Object
Dim EditBody As Body2
Dim IconFiles As System.Object
Dim Options As System.Integer
Dim value As Feature
 
value = instance.InsertMacroFeature2(BaseName, ProgId, MacroMethods, ParamNames, ParamTypes, ParamValues, DimTypes, DimValues, EditBody, IconFiles, Options)
```

```

Feature InsertMacroFeature2( 
   System.string BaseName,
   System.string ProgId,
   System.object MacroMethods,
   System.object ParamNames,
   System.object ParamTypes,
   System.object ParamValues,
   System.object DimTypes,
   System.object DimValues,
   Body2 EditBody,
   System.object IconFiles,
   System.int Options
)
```

```

Feature^ InsertMacroFeature2( 
   System.String^ BaseName,
   System.String^ ProgId,
   System.Object^ MacroMethods,
   System.Object^ ParamNames,
   System.Object^ ParamTypes,
   System.Object^ ParamValues,
   System.Object^ DimTypes,
   System.Object^ DimValues,
   Body2^ EditBody,
   System.Object^ IconFiles,
   System.int Options
) 
```

#### Parameters

*BaseName*

*ProgId*

*MacroMethods*

*ParamNames*

*ParamTypes*

*ParamValues*

*DimTypes*

*DimValues*

*EditBody*

*IconFiles*

*Options*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
