# PropagateToTangentFaces Property (IVariableFilletFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2~PropagateToTangentFaces`

Gets or sets whether to extend the fillet to all faces tangent to the selected face or edge.
Gets or sets whether to extend the fillet to all faces tangent to the selected face or edge.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PropagateToTangentFaces As System.Boolean
```

```

Dim instance As IVariableFilletFeatureData2
Dim value As System.Boolean
 
instance.PropagateToTangentFaces = value
 
value = instance.PropagateToTangentFaces
```

```

System.bool PropagateToTangentFaces {get; set;}
```

```

property System.bool PropagateToTangentFaces {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to extend fillet to all faces tangent to the selected face or edge, false to not

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IVariableFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2.md)  
[IVariableFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.md)
