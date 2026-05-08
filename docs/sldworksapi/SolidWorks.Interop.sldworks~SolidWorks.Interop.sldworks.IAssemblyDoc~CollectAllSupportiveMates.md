# CollectAllSupportiveMates Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CollectAllSupportiveMates`

Gets all mates supportive of a mate controller in this assembly.
Gets all mates supportive of a mate controller in this assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CollectAllSupportiveMates() As System.Object
```

```

Dim instance As IAssemblyDoc
Dim value As System.Object
 
value = instance.CollectAllSupportiveMates()
```

```

System.object CollectAllSupportiveMates()
```

```

System.Object^ CollectAllSupportiveMates(); 
```

#### Return Value

Array of supportive [mates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)

Remarks

This method is valid only if [IAssemblyDoc::IsSupportedMatesAvailable](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IsSupportedMatesAvailable.md) is true.

To create a mate controller, see the Remarks section of [IMateControllerFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.md).

For more information about the Mate Controller feature, see the **SOLIDWORKS user-interface help > Assemblies > Mates > Mate Controller** topic.

Example

See the [IMateControllerFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
