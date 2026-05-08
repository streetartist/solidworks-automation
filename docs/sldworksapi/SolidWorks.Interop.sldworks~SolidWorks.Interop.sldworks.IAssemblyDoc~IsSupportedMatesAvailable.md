# IsSupportedMatesAvailable Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IsSupportedMatesAvailable`

Gets whether this assembly contains mates that are supportive of a mate controller.
Gets whether this assembly contains mates that are supportive of a mate controller.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property IsSupportedMatesAvailable As System.Boolean
```

```

Dim instance As IAssemblyDoc
Dim value As System.Boolean
 
value = instance.IsSupportedMatesAvailable
```

```

System.bool IsSupportedMatesAvailable {get;}
```

```

property System.bool IsSupportedMatesAvailable {
   System.bool get();
}
```

#### Property Value

True if mates supportive of a mate controller are available, false if not

Remarks

Supportive mate types are as defined by [swMateType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMateType_e.html).:

- swMateANGLE
- swMateDISTANCE
- swMatePATH
- swMateSLOT
- swMateWIDTH

The Mate Controller feature does not support path, width, or slot mates created with either a free or a center in slot constraint.

If this property is true, then use [IAssemblyDoc::CollectAllSupportiveMates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CollectAllSupportiveMates.md) to collect the supportive mates in this assembly.

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
