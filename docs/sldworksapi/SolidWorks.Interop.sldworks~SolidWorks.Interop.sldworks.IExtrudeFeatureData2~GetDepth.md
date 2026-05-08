# GetDepth Method (IExtrudeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDepth`

Gets the depth of the extrusion feature in the forward or reverse direction.
Gets the depth of the extrusion feature in the forward or reverse direction.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDepth( _
   ByVal Forward As System.Boolean _
) As System.Double
```

```

Dim instance As IExtrudeFeatureData2
Dim Forward As System.Boolean
Dim value As System.Double
 
value = instance.GetDepth(Forward)
```

```

System.double GetDepth( 
   System.bool Forward
)
```

```

System.double GetDepth( 
   System.bool Forward
) 
```

#### Parameters

*Forward*
:   True for forward feature direction, false for reverse

#### Return Value

Depth of the extrusion

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)  
[IExtrudeFeatureData2::SetDepth Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetDepth.md)
