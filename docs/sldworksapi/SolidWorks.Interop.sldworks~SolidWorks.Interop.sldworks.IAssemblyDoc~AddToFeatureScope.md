# AddToFeatureScope Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddToFeatureScope`

Adds a component to the scope of the currently selected assembly feature.
Adds a component to the scope of the currently selected assembly feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddToFeatureScope( _
   ByVal CompName As System.String _
) As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim CompName As System.String
Dim value As System.Boolean
 
value = instance.AddToFeatureScope(CompName)
```

```

System.bool AddToFeatureScope( 
   System.string CompName
)
```

```

System.bool AddToFeatureScope( 
   System.String^ CompName
) 
```

#### Parameters

*CompName*
:   Name of component to add

#### Return Value

True if added successfully, false otherwise

Remarks

If no assembly feature is selected, then this method adds a component to a list for use with the next assembly feature created.

Assembly features allow you to create a feature that affects multiple components in an assembly. For example, if you need a hole through two blocks so that you could bolt them together, you can create a hole as an assembly feature and make it go through both blocks.

The scope of the assembly feature determines which components are effected by this feature. In other words, it describes which components can contain the feature.

There are two ways to use the IAssemblyDoc::AddToFeatureScope method:

- When an assembly feature is selected, IAssemblyDoc::AddToFeatureScope adds a component to the assembly feature's scope. Any component in the scope of the assembly feature can be affected by the assembly feature.
- You can also use IAssemblyDoc::AddToFeatureScope to compile a group of components. The next assembly feature created (for example, [IFeatureManager::SimpleHole](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SimpleHole.md)) affects each of the components in the compiled group.

After completing these steps, use [IAssemblyDoc::UpdateFeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UpdateFeatureScope.md) to display the changes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
