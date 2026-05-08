# ReverseFaceNormal Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ReverseFaceNormal`

Gets or sets the Reverse Face Normal option when creating a face fillet between surface bodies.
Gets or sets the Reverse Face Normal option when creating a face fillet between surface bodies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReverseFaceNormal( _
   ByVal WhichFaceList As System.Integer _
) As System.Boolean
```

```

Dim instance As ISimpleFilletFeatureData2
Dim WhichFaceList As System.Integer
Dim value As System.Boolean
 
instance.ReverseFaceNormal(WhichFaceList) = value
 
value = instance.ReverseFaceNormal(WhichFaceList)
```

```

System.bool ReverseFaceNormal( 
   System.int WhichFaceList
) {get; set;}
```

```

property System.bool ReverseFaceNormal {
   System.bool get(System.int WhichFaceList);
   void set (System.int WhichFaceList, System.bool value);
}
```

#### Parameters

*WhichFaceList*
:   Face for Reverse Face Normal option as defined in [swSimpleFilletWhichFaces\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSimpleFilletWhichFaces_e.html)

#### Property Value

True if the Reverse Face Normal option is enabled, false if not

Example

See [ISimpleFilletFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.md)  
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.md)
