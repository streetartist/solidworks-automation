# ModifyItemsNameAndPath Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~ModifyItemsNameAndPath`

Modifies the specified reference components with the specified names and paths.
Modifies the specified reference components with the specified names and paths.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ModifyItemsNameAndPath( _
   ByVal IdsList As System.Object, _
   ByVal NamesList As System.Object, _
   ByVal PathsList As System.Object _
) As System.Integer
```

```

Dim instance As IAdvancedSaveAsOptions
Dim IdsList As System.Object
Dim NamesList As System.Object
Dim PathsList As System.Object
Dim value As System.Integer
 
value = instance.ModifyItemsNameAndPath(IdsList, NamesList, PathsList)
```

```

System.int ModifyItemsNameAndPath( 
   System.object IdsList,
   System.object NamesList,
   System.object PathsList
)
```

```

System.int ModifyItemsNameAndPath( 
   System.Object^ IdsList,
   System.Object^ NamesList,
   System.Object^ PathsList
) 
```

#### Parameters

*IdsList*
:   Array of reference component IDs (see **Remarks**)

*NamesList*
:   Array of new reference component names

*PathsList*
:   Array of new reference component paths

#### Return Value

Return code as defined in [swSaveItemsPathError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSaveItemsPathError_e.html)

Remarks

Before calling this method call:

1. [IAdvancedSaveAsOptions::SetPrefixSuffixToAll](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~SetPrefixSuffixToAll.md)
2. [IAdvancedSaveAsOptions::GetItemsNameAndPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~GetItemsNameAndPath.md) to populate IDsList.

IdsList, NamesList, and PathsList are the same array size and map one to one. Use Nothing or null to specify no change to an individual reference in each array.

If you use this method to change the name or path of the top-level document, then it overrides the name or path passed in the Name parameter of [IModelDocExtension::SaveAs3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs3.md).

Example

See the [IAdvancedSaveAsOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedSaveAsOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.md)  
[IAdvancedSaveAsOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions_members.md)  
[IAdvancedSaveAsOptions::SaveAsPreviousVersion Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~SaveAsPreviousVersion.md)
