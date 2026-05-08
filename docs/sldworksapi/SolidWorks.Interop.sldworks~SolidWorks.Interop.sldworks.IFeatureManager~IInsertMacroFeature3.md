# IInsertMacroFeature3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertMacroFeature3`

Inserts a macro feature in this model.
Inserts a macro feature in this model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IInsertMacroFeature3( _
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
   ByVal BodyCount As System.Integer, _
   ByRef EditBodies As Body2, _
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
Dim BodyCount As System.Integer
Dim EditBodies As Body2
Dim IconCount As System.Integer
Dim IconFiles As System.String
Dim Options As System.Integer
Dim value As Feature
 
value = instance.IInsertMacroFeature3(BaseName, ProgId, MacroMethods, ParamCount, ParamNames, ParamTypes, ParamValues, DimCount, DimTypes, DimCountValues, BodyCount, EditBodies, IconCount, IconFiles, Options)
```

```

Feature IInsertMacroFeature3( 
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
   System.int BodyCount,
   ref Body2 EditBodies,
   System.int IconCount,
   ref System.string IconFiles,
   System.int Options
)
```

```

Feature^ IInsertMacroFeature3( 
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
   System.int BodyCount,
   Body2^% EditBodies,
   System.int IconCount,
   System.String^% IconFiles,
   System.int Options
) 
```

#### Parameters

*BaseName*
:   Name of the base feature (see **Remarks**)

*ProgId*
:   Indicates callback object (see **Remarks**)

*MacroMethods*
:   Null; valid only for VBA

*ParamCount*
:   Number of parameters

*ParamNames*
:   Array of strings of the parameters of size ParamCount

*ParamTypes*
:   Array of the types of parameters of size paramCount as defined by [swMacroFeatureParamType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMacroFeatureParamType_e.html)

*ParamValues*
:   Array of strings of the values of parameters of size ParamCount

*DimCount*
:   Number of dimensions

*DimTypes*
:   Array of the types of dimensions as defined by [swDimensionType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimensionType_e.html) (see **Remarks**)

*DimCountValues*
:   Array of doubles of the values of dimensions of size DimCount

*BodyCount*
:   Number of bodies to modify in the macro feature

*EditBodies*
:   Array of [IBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) objects to modify in the macro feature

*IconCount*
:   Number of icons

*IconFiles*
:   Array of strings of the file names for the icons (see **Remarks**)

*Options*
:   Placement of the macro feature in the FeatureManager design tree as defined by [swMacroFeatureOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMacroFeatureOptions_e.html) (see **Remarks**)

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

**BaseName**

- The argument BaseName is serialized within the feature and cannot be changed.
- You can find out the name of the base feature by using [IMacroFeatureData::GetBaseName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetBaseName.md).
- The BaseName argument is also used to generate the name of the feature when the feature is first created.

**ProgId**

| **If creating a macro feature using...** | **Then ProgId is...** |
| --- | --- |
| COM callback methods | The name of the component that implements the COM callback methods. The object that is represented by ProgID must support the ISwComFeature interface.  InsertMacroFeature3 ("Sample", "Sample.MyFeature", \_             Nothing, paramNames, paramTypes, \_                  paramValues, dimTypes, dimValues, \_                      editBodies, iconFiles, \_                      swMacroFeatureByDefault)  In the COM server, the Sample.Feature class is derived or supports the ISwComFeature interface. These methods support the macro feature's [rebuild](sldworksAPIProgGuide.chm::/Macro_Features/Rebuild_Function.htm), [edit](sldworksAPIProgGuide.chm::/Macro_Features/Edit_Definition_Function.htm), and [security](sldworksAPIProgGuide.chm::/Macro_Features/Security_Function.htm) functions. |

**DimTypes**

Only these dimension types are supported by this method:

- swAngularDimension
- swLinearDimension
- swRadialDimension

**IconFiles**

> The array of the file names for the icons can contain either three or nine strings.
>
> | Number of strings in array | Types of images in this order | Image format and sizes |
> | --- | --- | --- |
> | Three | 1. Regular 2. Suppressed 3. Highlighted | - Windows bitmap (**\*.bmp**) format - 16 pixels wide X 18 pixels high |
> | Nine  **NOTES:**   - This size array is only valid for macro features created in parts, assemblies, and drawings in SOLIDWORKS 2017 and later. - SOLIDWORKS displays the appropriate images based on the current DPI setting of the display device. | 1. Regular small 2. Suppressed small 3. Highlighted small 4. Regular medium 5. Suppressed medium 6. Highlighted medium 7. Regular large 8. Suppressed large 9. Highlighted large | - Windows bitmap (**\*.bmp**) format - Recommended sizes are:   - Small: 20 pixels wide X 20 pixels high   - Medium: 32 pixels wide X 32 pixels high   - Large: 40 pixels wide X 40 pixels high |
>
> You can specify either the full path name or just the file name for the strings; for example, c:\bitmaps\icon1.bmp or icon1.bmp.

**Options**

> swMacroFeatureOptions\_e.swMacroFeatureEmbedMacroFile is not supported by programming languages for the Microsoft .NET Framework; for example, not supported by C#, Visual Basic .NET, or Managed C++.

See [Overview of Macro Features](sldworksAPIProgGuide.chm::/Macro_Features/Overview_of_Macro_Features.htm) for more information.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IFeatureManager::InsertMacroFeature3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMacroFeature3.md)
