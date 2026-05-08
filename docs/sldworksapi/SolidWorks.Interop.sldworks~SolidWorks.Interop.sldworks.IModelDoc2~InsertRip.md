# InsertRip Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertRip`

Creates a rip feature.
Creates a rip feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertRip( _
   ByVal Gap As System.Double _
) 
```

```

Dim instance As IModelDoc2
Dim Gap As System.Double
 
instance.InsertRip(Gap)
```

```

void InsertRip( 
   System.double Gap
)
```

```

void InsertRip( 
   System.double Gap
) 
```

#### Parameters

*Gap*
:   Size of the rip gap

Remarks

The direction of the rip is determined by the Mark value used to select the edges along which to rip.

| Direction | Selection Mark | [IRipFeatureData::GetDirection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData~GetDirection.md) |
| --- | --- | --- |
| Current | 16 | 0 |
| Other | 32 | 1 |
| Both | 64 | 2 |

Example

[Access Edges on Rip Feature (VBA)](Access_and_Release_Access_to_Edges_Example_VB.htm)  
[Access Edges on Rip Feature (VB.NET)](Access_and_Release_Access_to_Edges_Example_VBNET.htm)  
[Access Edges on Rip Feature (C#)](Access_and_Release_Access_to_Edges_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IRipFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData.md)
