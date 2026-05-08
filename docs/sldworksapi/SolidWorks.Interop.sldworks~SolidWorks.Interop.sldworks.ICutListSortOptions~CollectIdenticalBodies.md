# CollectIdenticalBodies Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions~CollectIdenticalBodies`

Gets or sets whether to collect identical bodies into a cut list sub-folder.
Gets or sets whether to collect identical bodies into a cut list sub-folder.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CollectIdenticalBodies As System.Boolean
```

```

Dim instance As ICutListSortOptions
Dim value As System.Boolean
 
instance.CollectIdenticalBodies = value
 
value = instance.CollectIdenticalBodies
```

```

System.bool CollectIdenticalBodies {get; set;}
```

```

property System.bool CollectIdenticalBodies {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to collect identical bodies, false to not

Remarks

If set to true, this property puts all bodies that are geometrically identical, but generated in different features, into a cut list item sub-folder in the FeatureManager design tree.

If this is a weldment, identical bodies do not move between weldment sub-folders during the sort.

Example

See the [ICutListSortOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICutListSortOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions.md)  
[ICutListSortOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions_members.md)
