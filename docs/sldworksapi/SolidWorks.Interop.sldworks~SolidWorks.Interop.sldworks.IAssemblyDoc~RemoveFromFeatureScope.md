# RemoveFromFeatureScope Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~RemoveFromFeatureScope`

Removes a component from the scope of the currently selected assembly feature.
Removes a component from the scope of the currently selected assembly feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveFromFeatureScope( _
   ByVal CompName As System.String _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim CompName As System.String
Dim value As System.Boolean
 
value = instance.RemoveFromFeatureScope(CompName)
```

```

System.bool RemoveFromFeatureScope( 
   System.string CompName
)
```

```

System.bool RemoveFromFeatureScope( 
   System.String^ CompName
) 
```

#### Parameters

*CompName*
:   Name of component to remove

#### Return Value

True if successfully removed, false if not

Remarks

If no assembly feature is selected, this method removes a component from the list that is to be used with the next assembly feature created.

Assembly features allow you to create a feature that affects multiple components in an assembly. For example, if you need a hole through two blocks to bolt them together, you can create a hole as an assembly feature and make it go through both blocks.

The scope of the assembly feature determines which components are affected by this feature. In other words, it describes which components can contain the feature.

There are two ways to use the this technique:

- If you have an assembly feature selected, this method removes a component from the assembly features scope. Any component that is not in the scope of the assembly feature cannot be affected by the assembly feature.
- If you create a list of components, this method allows you to remove a component from the list. The next assembly feature created affects each of the components in your list.

After you use one of these techniques, you can use [IAssemblyDoc::UpdateFeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateFeatureScope.md) to display the changes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::UpdateFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateFeatureScope.md)  
[IAssemblyDoc::AddToFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddToFeatureScope.md)  
[IAssemblyDoc::GetFeatureScope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetFeatureScope.md)  
[IAssemblyDoc::GetFeatureScopeCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetFeatureScopeCount.md)
