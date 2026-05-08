# swBomTableSortItemGroup_e Enumeration

Help ID: `SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swBomTableSortItemGroup_e`

Categories for sorting bill of material table rows.
Categories for sorting bill of material table rows.

Syntax

- [Visual Basic](#Syntax-VBAll)
- [C#](#Syntax-CS)
- [Delphi](#Syntax-Delphi)
- [JScript](#Syntax-JScript)
- [Managed Extensions for C++](#Syntax-CPP)
- [C++/CLI](#Syntax-CPP2005)

```

'Declaration
 
```

```

<System.Runtime.InteropServices.GuidAttribute("069C7BF3-21D1-487C-A719-5E120617D49D")>
Public Enum swBomTableSortItemGroup_e 
   Inherits System.Enum
```

```

'Usage
 
```

```

Dim instance As swBomTableSortItemGroup_e
```

```

[System.Runtime.InteropServices.Guid("069C7BF3-21D1-487C-A719-5E120617D49D")]
public enum swBomTableSortItemGroup_e : System.Enum 
```

```

public enum swBomTableSortItemGroup_e = class(System.Enum)
```

```

System.Runtime.InteropServices.GuidAttribute("069C7BF3-21D1-487C-A719-5E120617D49D")
public enum swBomTableSortItemGroup_e extends System.Enum
```

```

[System.Runtime.InteropServices.Guid("069C7BF3-21D1-487C-A719-5E120617D49D")]
__value public enum swBomTableSortItemGroup_e : public System.Enum 
```

```

[System.Runtime.InteropServices.Guid("069C7BF3-21D1-487C-A719-5E120617D49D")]
public enum class swBomTableSortItemGroup_e : public System.Enum 
```

Members

| Member | Description |
| --- | --- |
| **swBomTableSortItemGroup\_Assemblies** | 1 = Group table rows containing assemblies |
| **swBomTableSortItemGroup\_None** | DO NOT USE |
| **swBomTableSortItemGroup\_Other** | 3 = Group table rows containing user-defined items |
| **swBomTableSortItemGroup\_Parts** | 2 = Group table rows containing parts |

Remarks

These enumerator options are used by [IBomTableSortData::ItemGroups](ms-help://SolidWorks.Interop.sldworks/SolidWorks/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTableSortData~ItemGroups.html) to set the groupings for table sorting.

For example, when you set IBomTableSortData::ItemGroups to the following array, assemblies are grouped first, parts are grouped second, and other categories are grouped last:

1. [swBomTableSortItemGroup\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomTableSortItemGroup_e.html).swBomTableSortItemGroup\_Assemblies
2. [swBomTableSortItemGroup\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomTableSortItemGroup_e.html).swBomTableSortItemGroup\_Parts
3. [swBomTableSortItemGroup\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBomTableSortItemGroup_e.html).swBomTableSortItemGroup\_Other

Inheritance Hierarchy

System.Object  
   System.ValueType  
      System.Enum  
         **SolidWorks.Interop.swconst.swBomTableSortItemGroup\_e**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[SolidWorks.Interop.swconst Namespace](SolidWorks.Interop.swconst~SolidWorks.Interop.swconst_namespace.md)
