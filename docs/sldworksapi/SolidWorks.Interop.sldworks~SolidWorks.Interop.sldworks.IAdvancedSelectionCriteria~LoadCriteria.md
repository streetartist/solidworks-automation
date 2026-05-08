# LoadCriteria Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~LoadCriteria`

Loads the specified query file and makes it the current advanced component selection criteria list.
Loads the specified query file and makes it the current advanced component selection criteria list.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function LoadCriteria( _
   ByVal CriteriaFileName As System.String _
) As System.Boolean
```

```

Dim instance As IAdvancedSelectionCriteria
Dim CriteriaFileName As System.String
Dim value As System.Boolean
 
value = instance.LoadCriteria(CriteriaFileName)
```

```

System.bool LoadCriteria( 
   System.string CriteriaFileName
)
```

```

System.bool LoadCriteria( 
   System.String^ CriteriaFileName
) 
```

#### Parameters

*CriteriaFileName*
:   Path and filename of query file (see **Remarks**)

#### Return Value

True if query file loads, false if not

Remarks

Specify CriteriaFileName with either a **\*.xml** file or a legacy **\*.sqy** file.

To create a **\*.xml** query file, you can either:

- Use the Advanced Component Selection dialog (**Standard toolbar > Advanced Select**) to export a query file in XML format.

    - or -

- Open a txt file in Notepad and add content as follows:

<?xml version="1.0" encoding="UTF-8"?>  
<SWQueryList>  
    <Query Name="InContextHasMate" Favourites\_Index="1">  
     <Boolean Name="And" Category="In Context Relations" SubCategory="Has mate to part" Condition="=" Value="base plate-1@98food processor"/>  
 </Query>  
</SWQueryList>

1. Replace the attribute values in the <Query> and <Boolean> elements as required. Refer to the **Assemblies > Basic Component Operations > Selecting Components > Advanced Component Selection > Search Criteria for Advanced Component Selection** topic in the SOLIDWORKS help to see all the options for populating the Category (Category1 in the dialog), SubCategory (Category2 in the dialog), Condition, and Value attributes.
2. In <Query> Favourites\_Index specifies where the query appears at the end of the Select toolbar. This attribute corresponds to the row number in the Manage Searches tab of the dialog.
3. In <Boolean> Name specifies "And" (default) or "Or" to indicate whether to logically AND or OR multiple Boolean elements in the Query element. This attribute corresponds to the And/Or column in the dialog.
4. Add more <Query> and <Boolean> elements as needed to further constrain your query.
5. Save the query file with a **.xml** extension.

After calling this method, call [IAdvancedSelectionCriteria::Select](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~Select.md) to select the assembly components that satisfy the query criteria.

Example

See the [IAdvancedSelectionCriteria](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedSelectionCriteria Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria.md)  
[IAdvancedSelectionCriteria Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria_members.md)
