# ItemGroups Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData~ItemGroups`

Gets and sets the categories into which the BOM table rows are grouped.
Gets and sets the categories into which the BOM table rows are grouped.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ItemGroups As System.Object
```

```

Dim instance As IBomTableSortData
Dim value As System.Object
 
instance.ItemGroups = value
 
value = instance.ItemGroups
```

```

System.object ItemGroups {get; set;}
```

```

property System.Object^ ItemGroups {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of categories as defined in [swBomTableSortItemGroup\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomTableSortItemGroup_e.html) or null (see **Remarks**)

Remarks

You can set this property in one of two ways:

- Specify null to indicate that the BOM table rows are not to be grouped into categories.
- Specify an array of [swBomTableSortItemGroup\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomTableSortItemGroup_e.html) enumerators to indicate that the BOM table rows are to be grouped into categories (assemblies, parts, user defined).

For example, when you set this property to an array of three enumerators in the following order, assemblies are grouped first, parts are grouped next, and user-defined categories are grouped last:

1. [swBomTableSortItemGroup\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomTableSortItemGroup_e.html).swBomTableSortItemGroup\_Assemblies
2. [swBomTableSortItemGroup\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomTableSortItemGroup_e.html).swBomTableSortItemGroup\_Parts
3. [swBomTableSortItemGroup\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomTableSortItemGroup_e.html).swBomTableSortItemGroup\_Other

To eliminate grouping into a category, do not include it in the array.

For example, when you set this property to the following array, no assemblies are grouped, parts are grouped first, and user-defined categories are grouped last:

1. [swBomTableSortItemGroup\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomTableSortItemGroup_e.html).swBomTableSortItemGroup\_Parts
2. [swBomTableSortItemGroup\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomTableSortItemGroup_e.html).swBomTableSortItemGroup\_Other

Example

See the [IBomTableSortData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomTableSortData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData.md)  
[IBomTableSortData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData_members.md)
