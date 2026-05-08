# SortCutList Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~SortCutList`

Sorts the cut list.
Sorts the cut list.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SortCutList( _
   ByVal CutListSortOptions As System.Object, _
   ByVal IgnoreInvalidFacesOrFeatures As System.Boolean _
) As System.Boolean
```

```

Dim instance As IBodyFolder
Dim CutListSortOptions As System.Object
Dim IgnoreInvalidFacesOrFeatures As System.Boolean
Dim value As System.Boolean
 
value = instance.SortCutList(CutListSortOptions, IgnoreInvalidFacesOrFeatures)
```

```

System.bool SortCutList( 
   System.object CutListSortOptions,
   System.bool IgnoreInvalidFacesOrFeatures
)
```

```

System.bool SortCutList( 
   System.Object^ CutListSortOptions,
   System.bool IgnoreInvalidFacesOrFeatures
) 
```

#### Parameters

*CutListSortOptions*
:   [ICutListSortOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions.md)

*IgnoreInvalidFacesOrFeatures*
:   True to sort bodies ignoring any invalid excluded faces/features, false to not sort the bodies if there are invalid excluded faces/features (see **Remarks**)

#### Return Value

True if sorting is successful, false if not

Remarks

Use [IBodyFolder::GetCutListSortOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder~GetCutListSortOptions.md) to populate CutListSortOptions.

This method applies the CutListSortOptions settings, sorts the cut list, and refreshes the cut list in the FeatureManager design tree.

In the Cut List Sorting Options PropertyManager you select faces/features to exclude from sorting. If some of those selected faces/features to exclude are invalid, i.e., they are not of selection type BODYFEATURE or FACE or they cannot be excluded (see the end of this **Remark**), a dialog box pops up during the sort operation with:

----------------------------------------------------------------------

**Failed to exclude some of the selected faces in cut list sorting. Try selecting the corresponding features instead.**

**Would you like to continue:**

**Yes (Bodies will be sorted ignoring some of the excluded faces.)**

**No (Bodies will not be sorted.)**

**----------------------------------------------------------**

IgnoreInvalidFacesOrFeatures handles the situation when some of the body faces/features selected for exclusion ([ICutListSortOptions::SetFacesOrFeaturesToExclude](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions~SetFacesOrFeaturesToExclude.md)) can not be excluded.

Set IgnoreInvalidFacesOrFeatures to:

- True, to sort bodies ignoring any invalid excluded faces/features.
- False, to not sort the bodies if there are invalid excluded faces/features.

If you set IgnoreInvalidFacesOrFeatures to false and there are invalid faces/features in the exclusion list, then this method will not sort the cut list.

Other examples of faces and features that are invalid for exclusion:

- Chamfers that remove an entire face.
- Suppressed features.
- Features that create new bodies from sketches, such as boss-extrude, revolve, and sweep.
- Certain sheet metal features.

For more information, see the **Sorting Cut Lists** topics in the SOLIDWORKS user-interface help.

Example

See the [IBodyFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBodyFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder.md)  
[IBodyFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder_members.md)
