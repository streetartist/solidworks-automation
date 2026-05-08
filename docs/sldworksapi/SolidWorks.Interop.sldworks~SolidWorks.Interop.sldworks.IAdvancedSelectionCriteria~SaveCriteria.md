# SaveCriteria Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~SaveCriteria`

Saves the current query to the specified XML file.
Saves the current query to the specified XML file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SaveCriteria( _
   ByVal CriteriaFileName As System.String _
) As System.Boolean
```

```

Dim instance As IAdvancedSelectionCriteria
Dim CriteriaFileName As System.String
Dim value As System.Boolean
 
value = instance.SaveCriteria(CriteriaFileName)
```

```

System.bool SaveCriteria( 
   System.string CriteriaFileName
)
```

```

System.bool SaveCriteria( 
   System.String^ CriteriaFileName
) 
```

#### Parameters

*CriteriaFileName*
:   Path and filename (**\*.xml**) to which to save the current query

#### Return Value

True if current query is saved successfully, false if not

Remarks

Call this method after [adding](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~AddItem2.md) criteria to the current advanced component selection criteria list.

As of SOLIDWORKS 2021, you can save queries only in XML format.

As is done using the Advanced Component Selection dialog (**Standard toolbar > Advanced Select**), this method creates a query file in XML format with one or more <Query> and <Boolean> elements. Each <Query> element represents a particular search by Category (Category1 in the user interface) and SubCategory (Category2 in the user interface) to satisfy a Condition expression:

?xml version="1.0" encoding="UTF-8"?>  
<SWQueryList>  
   <Query Name="SelectPegs" Favourites\_Index="1">  
      <Boolean Name="And" Category="Custom Property" SubCategory="IsPeg" Condition="=" Value="Yes"/>  
   </Query>  
   <Query Name="SelectBlockParts" Favourites\_Index="2">  
      <Boolean Name="And" Category="Custom Property" SubCategory="IsBlockPart" Condition="=" Value="Yes"/>  
   </Query>  
</SWQueryList>

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedSelectionCriteria Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria.md)  
[IAdvancedSelectionCriteria Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria_members.md)
